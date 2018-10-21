import subprocess
import os

class Pythuby:

    def __init__(self, code = False, file = False):
        if code:
            self.code = code
            self.pythuby()
        if file:
            self.file = file

    def pythuby(self):
        with open("Temp.rb", "w") as temp_rb_script:
            temp_rb_script.write(self.code)
            temp_rb_script.close()


    def runPythuby(self):
        cmd = subprocess.Popen("ruby Temp.rb", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result = cmd.stdout.read().decode("UTF-8")
        #os.remove("Temp.rb")
        return (result)

    def include(self, file):
        cmd = subprocess.Popen("ruby {}".format(file), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = (cmd.stdout.read() + cmd.stderr.read()).decode("UTF-8")
        return (result)
