import string

def generate_testbench(num_tests, data_width):
  # Initialize the testbench string
  testbench = ""

  # Add the module declaration
  testbench += f"module testbench();\n\n"

  # Add the SDRAM controller instance
  testbench += f"  SDRAMController ctrl(.clk(clk), .reset(reset), .data_width({data_width}));\n\n"

  # Add the test case function
  testbench += "  function void run_tests();\n"
  testbench += "    initial begin\n"

  # Generate the test cases
  for i in range(num_tests):
    address = f"16'h{i:04x}"  # Generate a hexadecimal address
    data = f"{data_width}'h{i:x}"  # Generate a hexadecimal data value
    testbench += f"      ctrl.write({address}, {data});\n"
    testbench += f"      assert(ctrl.read({address}) == {data});\n"

  testbench += "    end\n"
  testbench += "  endfunction\n"
  testbench += "\n"

  # Add the initial block
  testbench += "  initial begin\n"
  testbench += "    clk = 1'b0;\n"
  testbench += "    forever #5 clk = ~clk;\n"
  testbench += "  end\n"
  testbench += "endmodule\n"

  return testbench

# Generate a testbench with 10 test cases and a data width of 32 bits
testbench = generate_testbench(10, 32)

# Print the testbench
print(testbench)
