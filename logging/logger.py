import logging

logging.basicConfig(filename="myfile.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S")

