require "open3"

class Rubython

  attr_reader :return_value

  def initialize(code: false, file: false)
    if code
      @code = code
      rubython
      runRubython

    elsif file
      run_from_file(file)
    end
  end

  def rubython ()
    temp_py_script = File.open("Temp.py", "w")
    temp_py_script.write(@code)
    temp_py_script.close
  end

  def run_rubython
    Open3.popen3("python Temp.py") do |stdin, stdout, stderr|
      @return_value = stdout.read
      @stderr = stderr.read
    end
    File.delete("Temp.py")
  end

  def run_from_file(file)
    Open3.popen3("python #{file}") do |stdin, stdout, stderr|
      @return_value = stdout.read
      @stderr = stderr.read
    end
  end
end


