import sys

class RelationError(Exception):
    def error_info(self, message = "Relation Failure"):
        self.exception_type, self.exception_object, self.exception_traceback = sys.exc_info()
        filename = self.exception_traceback.tb_frame.f_code.co_filename
        line_number = self.exception_traceback.tb_lineno
        print("Exception type: ", self.exception_type)
        # print("Exception Object: ", self.exception_object)
        print("Message: ", message)
        print("File name: ", filename)
        print("Line number: ", line_number)

# try:
#     raise RelationError
# except RelationError as e:
#     # RelationError("Eras ")
#     e.error_info("Error")


    # exception_type, exception_object, exception_traceback = sys.exc_info()
    # filename = exception_traceback.tb_frame.f_code.co_filename
    # line_number = exception_traceback.tb_lineno
    # # print("Exception type: ", exception_type)
    # print("Message: ", exception_object)
    # print("File name: ", filename)
    # print("Line number: ", line_number)

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# try:
#     raise NotImplementedError("Not implemented")
# except Exception as e:
#     exception_type, exception_object, exception_traceback = sys.exc_info()
#     filename = exception_traceback.tb_frame.f_code.co_filename
#     line_number = exception_traceback.tb_lineno
#     print("Exception type: ", exception_type)
#     print(exception_object)
#     print("File name: ", filename)
#     print("Line number: ", line_number)
