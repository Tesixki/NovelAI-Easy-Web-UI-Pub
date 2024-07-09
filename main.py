import asyncio
import io
import json
from pathlib import Path
import random
from datetime import datetime
import gradio as gr
from PIL import Image
from boilerplate import API
from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset

# promptが記入されているjsonファイルを読み込む
with open("prompt.json", "r", encoding="utf-8") as f:
    options = json.load(f)

# NovelAI APIを利用して画像を生成する
async def main(
    hair_color,
    eye_color,
    hair_style,
    clothes,
    facial_expressions,
    characteristic,
    composition,
    pose,
    background,
    style,
    resolution,
    additional_prompt,
):
    # 画像を保存するディレクトリを作成
    d = Path("results")
    d.mkdir(exist_ok=True)

    # APIキーの取得
    async with API() as api_handler:
        api = api_handler.api

        # モデルの指定
        model = ImageModel.Anime_v3
        preset = ImagePreset.from_default_config(model)

        # プロンプトの結合
        prompt = f"rating:general, {additional_prompt}{background}{style}{hair_color}{hair_style}{eye_color}{clothes}{characteristic}{composition}{pose}{facial_expressions}1girl, "

        #　NovelAIの品質タグプリセット
        preset.uc_preset = "Preset_Heavy"

        # ネガティブプロンプト
        preset.uc = "{{{nail}}}, animal, no_human, +_+, {{hair_ornament}}, hairpin, [[bikini]], "

        # シードの指定とシードのランダム化
        preset.seed = random.randint(1, 9999999999)

        # 解像度の指定
        preset.resolution = resolution

        # サンプラーの指定
        preset.sampler = "k_euler_ancestral"

        #　スケールの指定
        preset.scale = 5.5

        # オートSMEAの有効・無効
        #preset.auto_smea = True

        # SMEAの有効・無効
        preset.smea = True

        # DYNの有効・無効
        preset.smea_dyn = False

        # プロンプトを反映する正確度の再調整の指定
        preset.cfg_rescale = 0.3

        # ノイズ設定の指定
        preset.noise_schedule = "native"

        # NovelAI APIを利用して画像を生成
        async for _, img in api.high_level.generate_image(prompt, model, preset):
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = d / f"image_{current_time}.png"
            image_path.write_bytes(img)
            return img


def run_main(
    hair_color,
    eye_color,
    hair_style,
    clothes,
    facial_expressions,
    pose,
    characteristic,
    composition,
    background,
    style,
    resolution,
    additional_prompt,
):
    selected_hair_color = options["hair_color"][hair_color]
    selected_eye_color = options["eye_color"][eye_color]
    selected_hair_style = options["hair_style"][hair_style]
    selected_clothes = options["clothes"][clothes]
    selected_facial_expressions = options["facial_expressions"][facial_expressions]
    selected_pose = options["pose"][pose]
    selected_characteristic = options["characteristic"][characteristic]
    selected_composition = options["composition"][composition]
    selected_background = options["background"][background]
    selected_style = options["style"][style]
    selected_resolution = tuple(options["resolution"][resolution])

    image_bytes = asyncio.run(
        main(
            selected_hair_color,
            selected_eye_color,
            selected_hair_style,
            selected_clothes,
            selected_facial_expressions,
            selected_pose,
            selected_characteristic,
            selected_composition,
            selected_background,
            selected_style,
            selected_resolution,
            additional_prompt,
        )
    )

    image = Image.open(io.BytesIO(image_bytes))
    return image


# Create Gradio interface
iface = gr.Interface(
    fn=run_main,
    inputs=[
        gr.Dropdown(
            choices=list(options["hair_color"].keys()), label="髪の色", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["eye_color"].keys()), label="目の色", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["hair_style"].keys()), label="髪型", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["clothes"].keys()), label="服装", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["facial_expressions"].keys()),
            label="表情",
            value="指定なし",
        ),
        gr.Dropdown(
            choices=list(options["pose"].keys()), label="ポーズ", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["characteristic"].keys()),
            label="特徴",
            value="指定なし",
        ),
        gr.Dropdown(
            choices=list(options["composition"].keys()), label="構図", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["background"].keys()), label="背景", value="指定なし"
        ),
        gr.Dropdown(
            choices=list(options["style"].keys()), label="絵柄", value="標準"
        ),
        gr.Dropdown(
            choices=list(options["resolution"].keys()),
            label="解像度",
            value="縦長 (832x1216)",
        ),
        gr.Textbox(
            label="追加のプロンプト",
            placeholder="ここに追加のプロンプトを入力してください"
        ),
    ],
    outputs=gr.Image(type="pil", label="生成された画像", format="png"),
    live=False,
    allow_flagging="never",
)

iface.launch(inbrowser=True)