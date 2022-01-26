import random

values = []
values.append([1]*5)
values.append([2]*5)
values.append([3]*5)
values.append([4]*5)
values.append([5]*3)
values.append([6]*3)
values = [v for vals in values for v in vals]
with open('current-letters.html', 'w') as page:
    page.write('''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Bomb Belt Current Letter Values</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
</head>
<body class="bg-dark">
    <div class="container text-light">
    <div class="col-md-5">
    </div>
        <table class="table text-light">
            <thead>
                <tr>
                    <th>Letter</th>
                    <th>Value</th>
                    <th></th>
                    <th>Letter</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>\n''')
    for letter in range(65, 78):
        a = random.choice(values)
        values.remove(a)
        b = random.choice(values)
        values.remove(b)
        page.write(f'                <tr><td>{chr(letter)}</td><td>{a}</td><td></td><td>{chr(letter+13)}</td><td>{b}</td></tr>\n')
    page.write('''                <tr></tr>
        </table>
</div>
</body>
</html>''')