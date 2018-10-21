import subprocess
import os

class Pythuby:

    def __init__(self, code = False, file = False):
        if code:
            self.code = code

        if file:
            self.file = file

    def pythuby(self):
        with open("Temp.rb", "w") as temp_rb_script:
            temp_rb_script.write(self.code)
            temp_rb_script.close()
            self.runPythuby()

    def runPythuby(self):
        cmd = subprocess.Popen("ruby Temp.rb", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result = cmd.stdout.read()
        #os.remove("Temp.rb")
        #return (result)

    def inculde(self):
        cmd = subprocess.Popen("ruby {}".format(self.file), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = cmd.stdout.read() + cmd.stderr.read()
        return (result)



code = "a = [1,2,3,4,5,6,7]\n" \
       "a.each do |e|\n" \
       "puts e.odd?\n" \
       "end"

a = Pythuby(code = code, file=False)
print(a.pythuby())
print(a)