from ascii_ctf import *

db.create_all()

def declare_chal(data):
    chal = Challenges.query.filter_by(name=data["name"]).first()
    if chal is not None:
        for n in data:
            if n == "name": continue
            setattr(chal, n, data[n])
    else:
        data["solves"] = "0"
        data["score"] = str(MAX_SCORE)
        db.session.add(Challenges(**data))
    db.session.commit()


declare_chal({
    "name": "Challenge 1",
    "category": "pwn",
    "info": """
Data: <a href="https://foo.bar/chal1.zip">chal1.zip</a>
Host: 666.666.666.666
Port: 31337

Hello world.
""",
    "flag": 'flag{xxxxxxxxxxxxxx}'
})


