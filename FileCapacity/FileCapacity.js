var objFSO = new ActiveXObject("Scripting.FileSystemObject");
var Shell = new ActiveXObject("Shell.Application")
var objFolder = Shell.BrowseForFolder( 0, "�t�H���_�I��", 0, "D:\\" );
if(!objFolder) {
�@�@WScript.Echo("�t�H���_��I�����Ă�������");
�@�@WScript.Quit();
}


var objFolderItems = objFolder.Items();
var ARRAY = new Array();
for (var a=0; a<objFolderItems.Count; a++)
{
�@�@�@�@var objItem = objFolderItems.Item(a);
�@�@�@�@if (objFSO.GetExtensionName(objItem) == "psd")
�@�@�@�@�@�@�@�@{
�@�@�@�@�@�@�@�@var Num = Number(objItem.Size);
�@�@�@�@�@�@�@�@ARRAY.push(Num);
�@�@�@�@�@�@�@�@}
}
var objFSO = "";
var FI ="0" ;
var FA = "-1" ;
var KB = "1048576";
for (var b=0; b<ARRAY.length; b++)
{
�@�@�@�@var OP = Number(ARRAY[b]);
�@�@�@�@FI = FI - OP;
}
FI = FI * FA;
FI = FI / KB;
FI = FI * "1000";
FI = Math.round(FI);
FI = FI / "1000";
WScript.Echo("�e�ʂ�"+FI+ "MB�ɂȂ�܂�");