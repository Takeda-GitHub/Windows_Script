# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name: fileCheck.py
# Purpose: �X�N���v�g��z�u�����t�H���_�Ńe�L�X�g���Q�Ƃ���
#�@�@�@�@�@�@�@�L�ڂ��Ȃ����̂���������A�\�������肷��v���O�C��
#�@�@�@�@�@�@�@�g�����͏�L�ɏ����Ă���ʂ�A�e�L�X�g�Ɣ�r�������t�H���_��
#�@�@�@�@�@�@�@���̃X�N���v�g��z�u���āA��r�Ώۂ̃e�L�X�g���ulist_base.txt�v�Ƃ���
#�@�@�@�@�@�@�@�z�u���ĉ������B���Ƃ͎��s���邾���ł��B
#�@�@�@�@�@�@�@���삷��ꍇ�͍ŏI�s��F�X�J�X�^���������B
#
#-------------------------------------------------------------------------------
 
import os # os���W���[���̃C���|�[�g
import re # ���K�\�����W���[���̃C���|�[�g
 
# os.listdir('�p�X')�z��Ƀt�@�C�����i�[
files = os.listdir(os.path.dirname(__file__))
pick = []#��̔z���p��
obj_del = []
f = open('list_base.txt','r')#��������t�@�C���ꗗ������e�L�X�g���J���A�z��Ŏ擾
 
for k in f.readlines():
pick.append(k)#���x�ێ��ׁ̈A��x�z��Ɋi�[
f.close()
a_str = map(str,pick)#�Ȃ�ƂȂ�������̕����T�[�`�������悤�ȋC�������̂ŕ�����
del_joint = ",".join(a_str)#�J���}�ŋ�؂�����
 
for file in files:
basename, extension = os.path.splitext(file)#�X�s���b�g���āA�g���q���擾
if extension == ".txt" or extension == ".csv":#�ꉞ�e�L�X�g��CSV���w��B�����ƂȂ��B
Find_name = re.search (file, del_joint)#pick�ł͎g���Ă��Ȃ��t�@�C�����擾
if Find_name is None:
os.remove(file)
