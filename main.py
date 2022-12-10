import streamlit as st
import os
import random

CSS = """
body {
    background-color: #afeeee;
  }
h1{
    text-align: center;
    color: #171246;
}
h2{
    color: rgb(24, 124, 45);;
}   
"""

st.header('HTML課題補助ツール')
st.markdown("***")
st.title("HTMLの内容を入力してください")
st.caption("パソコン推奨です。また、これは補助ツール（＝下書きを作るようなもの）なので、仕上げは各自行ってください。（そこまで難しくないはず！）")
st.caption("また、CSSや細かい部分は、先生に察せられるのを防ぐため各自変更することを推奨します（「アピールポイント」を「工夫した点」に変えたり、、、）")



HTML_list = {
            "TITLE":None,
            "USER":None,
            "APPEAL":None,
            "INTRO":None,
            "LINK":None,
            "IMAGE":None,
            "LIST":None,
            "TSOURCE":None,
            }

st.write("")
#タイトル
with st.form("TITLE"):
   HTML_list["TITLE"] = st.text_input('HTMLのタイトル', 'タイトルを入力してください')
   submitted = st.form_submit_button("完了")
   if submitted:
       st.write("入力済み")
st.write("")

#個人情報
with st.form("USER"):
    User_Class = st.text_input('あなたのクラス', 'クラスを入力')
    User_Num = st.text_input('あなたの出席番号', '出席番号を入力')
    User_Id = st.text_input('あなたの学籍番号', '学籍番号をを入力')
    User_Name = st.text_input('あなたの名前', '名前を入力')
    User = [User_Class, User_Num, User_Id, User_Name]
    HTML_list["USER"] = User
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")
#アピールポイント
with st.form("APPEAL"):
    HTML_list["APPEAL"] = st.text_area('アピールポイントを入力してください。', '・「〇〇を分かりやすくまとめられた」など')
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")
#まえがき
with st.form("INTRO"):
    Text_Title = st.text_input('まえがき')
    Text_Text = st.text_area('文章を入力')
    Text = [Text_Title, Text_Text]
    HTML_list["INTRO"] = Text
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")
#リンク
with st.form("LINK"):
    Link_title = st.text_input('URLのタイトルを入力')
    Url = st.text_input('URLを入力')
    Link = [Link_title, Url]
    HTML_list["LINK"] = Link
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")
#画像
with st.form("IMAGE"):
    Image = st.text_input('画像のURLを入力（リンク画像以外は各自でお願いします…）')
    HTML_list["IMAGE"] = Image
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")
#箇条書き
with st.form("LIST"):
    st.write("ここでの箇条書きは３つまでですが、増やしたり減らしたりしたい場合は各自でコードを編集なさってください")
    List_1 = st.text_input('箇条書き１つめ')
    List_2 = st.text_input('箇条書き２つめ')
    List_3 = st.text_input('箇条書き３つめ')
    List = [List_1, List_2, List_3]
    HTML_list["LIST"] = List
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")
#参考文献
with st.form("SOURCE"):
    Source = st.text_area("参考文献などを入力")
    HTML_list["SOURCE"] = Source
    submitted = st.form_submit_button("完了")
    if submitted:
        st.write("入力済み")
st.write("")





st.write("おまけ：CSS（色は各自変えてください）")
st.code(CSS,language="css")
if st.button("HTML出力"):
    HTML = rf"""
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>{ HTML_list["TITLE"] }</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>{ HTML_list["TITLE"] }</h1>
    <p>{ HTML_list["USER"][0] }組{ HTML_list["USER"][1] }番{ HTML_list["USER"][2] }{ HTML_list["USER"][3] }</p>
    <hr>
    <h2>アピールポイント</h2>
    <p>{ HTML_list["APPEAL"] }
    <p>

    <h2>{ HTML_list["INTRO"][0] }</h2>
    <p>{ HTML_list["INTRO"][1] }</p>

    <a href="{ HTML_list["LINK"][1] }">{ HTML_list["LINK"][0] }</a><br>

    <img src="{ HTML_list["IMAGE"] }"><br>

    <ul>
        <li>{ HTML_list["LIST"][0] }</li>
        <li>{ HTML_list["LIST"][1] }</li>
        <li>{ HTML_list["LIST"][2] }</li>
    </ul>
    <hr>
    <h2>参考文献</h2>
    <p>{ HTML_list["SOURCE"] }</p>


</body>

</html>
    """
    st.write("↓ファイルをダウンロード")
    st.download_button(
    label="HTMLファイルをダウンロード",
    data=HTML,
    file_name='index.html',
    mime='text/html',
    )
    st.code(HTML,language="html")