@echo off
REM �R�}���h�v�����v�g�̕����R�[�h��ݒ�
chcp 932 >nul

REM ���[�U�[�Ƀ��[���A�h���X�ƃp�X���[�h�̓��͂����߂�
set /p NAI_USERNAME=NovelAI�̃��[�U�[���i���[���A�h���X�j����͂��Ă�������: 
set /p NAI_PASSWORD=NovelAI�̃p�X���[�h����͂��Ă�������: 

REM .env�t�@�C���̍쐬
echo NAI_USERNAME=%NAI_USERNAME% > .env
echo NAI_PASSWORD=%NAI_PASSWORD% >> .env

REM venv�쐬���b�Z�[�W
echo venv�̍쐬���ł�

REM ���z���̍쐬
python -m venv venv

REM ���z�����A�N�e�B�u��
call venv\Scripts\activate

REM �p�b�P�[�W�C���X�g�[�����b�Z�[�W
echo �K�v�ȃp�b�P�[�W���C���X�g�[�����ł�

REM �K�v�ȃp�b�P�[�W���C���X�g�[��
pip install novelai-api==0.28.1 
pip install gradio==4.29.0 

REM �������b�Z�[�W
echo �Z�b�g�A�b�v���������܂����B���z�����쐬����A�p�b�P�[�W���C���X�g�[������A.env�t�@�C�����ݒ肳��܂����B
pause