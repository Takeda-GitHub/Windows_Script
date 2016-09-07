# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name: fileCheck.py
# Purpose: スクリプトを配置したフォルダでテキストを参照して
#　　　　　　　記載がないものを消したり、表示したりするプラグイン
#　　　　　　　使い方は上記に書いている通り、テキストと比較したいフォルダに
#　　　　　　　このスクリプトを配置して、比較対象のテキストも「list_base.txt」として
#　　　　　　　配置して下さい。あとは実行するだけです。
#　　　　　　　操作する場合は最終行を色々カスタム下さい。
#
#-------------------------------------------------------------------------------
 
import os # osモジュールのインポート
import re # 正規表現モジュールのインポート
 
# os.listdir('パス')配列にファイルを格納
files = os.listdir(os.path.dirname(__file__))
pick = []#空の配列を用意
obj_del = []
f = open('list_base.txt','r')#検索するファイル一覧があるテキストを開き、配列で取得
 
for k in f.readlines():
pick.append(k)#速度保持の為、一度配列に格納
f.close()
a_str = map(str,pick)#なんとなく文字列の方がサーチが早いような気がしたので文字列化
del_joint = ",".join(a_str)#カンマで区切り入れて
 
for file in files:
basename, extension = os.path.splitext(file)#スピリットして、拡張子を取得
if extension == ".txt" or extension == ".csv":#一応テキストとCSVを指定。※何となく。
Find_name = re.search (file, del_joint)#pickでは使われていないファイルを取得
if Find_name is None:
os.remove(file)
