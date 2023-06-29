from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content__(self):
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Контакты</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">


</head>
<body>
<h1 align="center">Контакты</h1>

<table>
    <tr>
        <td>
            <div class="row mt-3  gap-15">
                <div class="card" style="width: 30rem; left: 5rem;">
                    <form>
                        <div class="mb-3">
                            <label for="exampleCheck1" class="form-label">Имя</label>
                            <input type="text" class="form-control" id="exampleCheck1">
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputEmail1" class="form-label">Почта</label>
                            <input type="email" class="form-control" id="exampleInputEmail1"
                                   aria-describedby="emailHelp">
                        </div>
                        <div class="mb-3">
                            <label for="exampleCheck2" class="form-label">Сообщение</label>
                            <input type="text" class="form-control" id="exampleCheck2">
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
        </td>
        <td>
            <div class="blockquote gap-15">
                <div style="width: 10rem; left: 50rem; " align="left">
                </div>
        </td>
        <td>
            <div class="blockquote gap-15">
                <div style="width: 40rem; left: 50rem; " align="left">
                    <h3 align="left">Наши контакты</h3>
                    <div>A well-known quote, contained in a blockquote element.A well-known quote, contained in a
                        blockquote
                        element.
                        A well-known quote, contained in a blockquote element.A well-known quote, contained in a
                        blockquote
                        element.
                    </div>
                </div>
        </td>
    </tr>
</table>
        """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_content__()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
