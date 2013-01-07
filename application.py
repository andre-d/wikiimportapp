from flask import Flask, render_template_string, request
import markdowner
application = Flask(__name__)

_TEMPLATE = """
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>HTML to reddit markdown</title>
        <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container-fluid">
        <h1>reddit HTML to markdown converter</h1>
        <form method="POST" class="well">
            <label for="htmlinput">Paste your html into the box below:</label> 
            <textarea id="htmlinput" name="htmlinput" class="input-block-level" rows="5">{{ input }}</textarea>
            <input type="submit" value="Submit" class="btn btn-primary">
        </form>
        {%- if not output is none %}
            <h1>results</h1>
            <div class="well">
                <label for="markdownoutput">Below is your markdown output:</label> 
                <textarea id="markdownoutput" class="input-block-level" rows="5">{{ output }}</textarea>
            </div>
        {%- endif %}
    </div>
    </body>
</html>
"""

@application.route("/", methods=["GET", "POST"])
def mainpage():
    htmlinput = request.form.get("htmlinput", "")
    mdoutput = None
    if "htmlinput" in request.form:
        mdoutput = markdowner.markdownify(htmlinput)
    return render_template_string(_TEMPLATE, input=htmlinput, output=mdoutput)

if __name__ == "__main__":
    # app.debug = True # DO NOT UNCOMMENT ON PRODUCTION
    application.run()
