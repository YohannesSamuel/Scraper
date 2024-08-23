def generate_report(result):
    code = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
</head>
<body>
    <br>
    <br>
    <h1 style="font-size: 45px; font-family: Inter; text-align: center;"><span style="padding: 5px; border: 3px solid orange; margin-top: 20px; border-radius: 5px;">OSINT</span> TOOL</h1>
    <br>
    <h4 style="text-align: center; font-size: 20px;">[+] By Yohannes Samuel</h4>
    <br>
    <br>
    <br>
    <br>
    <div id="googlelab" class="button"><p>Google Dorking Results</p><button>^</button></div>
    <div id="google" class="result">
        <br><br><br>
        {result["dork"]}
    </div>
    <div id="tiktoklab" class="button"><p>Dark Web Scraping Results</p><button>^</button></div>
    <div id="tiktok" class="result">
        <br><br><br>
        {result["darkweb"]}
    </div>

</body>
<script src="script.js"></script>
</html>
    '''
    open("report.html", "wb").write(code.encode())

