class invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes ${self.total}'
    



google = invoice('Google', 100)
snapchat = invoice('Snapchat', 200)

print(google.formatter())
print(snapchat.formatter())