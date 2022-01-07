import dropbox

class TransferData():
    def __init__(self,access_token):
        self.access_token= access_token

    def upload_file():
        dbx=dropbox.Dropbox(self.access_token)
        f= open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Ipb42Y-1Cc8AAAAAAAAAASlrsc1i5jkkhB48dO-K3h8kYJcVuUSCuYGU6nHT53Z9'
    
    transferData = TransferData(access_token)

    file_from = input(" Enter the file path to transfer from : - ")
    file_to = input("Enter the full path to upload to dropbox:- ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved to Dropbox !!")


main()


