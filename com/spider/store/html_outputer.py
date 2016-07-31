import os


class HtmlOutputer(object):
    file_dir = "G:\\baike"
    file_index = 1

    def __init__(self):
        self.datas = []
        if not os.path.exists(self.file_dir):
            print(self.file_dir + ' not')
            os.mkdir(self.file_dir)

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open(os.path.join(self.file_dir, str(self.file_index)) + '.htm', 'w', encoding='utf8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table borderColor=#000000 height=40 cellPadding=0 width=100% align=center border=0>")
        fout.write("<tr><td>标题</td><td>内容</td></tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href=%s>%s</td>" % (data['url'], data['title']))
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")

        fout.write("</body>")
        fout.write("</html>")

        fout.close()


def file_split(file):
    file_size = os.path.getsize(file)
    print("file size:", file_size)
    if file_size > 50:
        return True
    return False
