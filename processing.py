"""
File: processing.py
Author: Wyatt Tauber

Includes processing support functions for the Razer Chroma covert channel
"""
import os
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile


def unzip_chroma(chroma_file, extract_folder):
    """
    Unzip a .ChromaEffects file to a folder
    :param chroma_file: filename of the .ChromaEffects file
    :param extract_folder: folder name that contains the extracted files
    :return: extract_folder
    """
    # make sure the file exists
    if not os.path.isfile(chroma_file):
        print("Error:", chroma_file, "does not exist.")
        quit()

    # extract all the contents of the file in the current directory
    # filenames will be 'name of zip'_'name of file.extension'
    with ZipFile(chroma_file, 'r') as chroma_zip_obj:
        for file_name in chroma_zip_obj.namelist():
            # only extract the chroma .xml files
            if file_name.endswith('.xml'):
                # extract the file
                chroma_zip_obj.extract(file_name, path=extract_folder)

                # rename the file to 'name of zip'_'name of file.extension'
                os.rename(extract_folder + "\\" + file_name, extract_folder + "\\" + chroma_file + "_" + file_name)

                # report that the file was extracted and add the filename to the list of extracted files
                print("\tExtracted", chroma_file + "_" + file_name)

    # return the folder name of the extracted files
    return extract_folder


def parse_xml(xml_file):
    """
    Parse the XML file
    :TODO: this is just a demo for now, figure out what we need to edit
    :param xml_file: the XML file to parse
    """
    # get the root of the XML
    root = ET.parse(xml_file).getroot()
    tag = root.tag

    # print the tag
    print("\t" + tag)


def zip_chroma(extract_folder, chroma_file):
    """
    Zip a folder to a .ChromaEffects file
    :param extract_folder: folder name that contains the extracted files
    :param chroma_file: filename of the .ChromaEffects file
    :return: chroma_file
    """
    # create the zip folder
    with ZipFile(chroma_file, 'w') as chroma_zip:
        # go through and zip the files in the directory
        for path, directories, files in os.walk(extract_folder):
            for file in files:
                # restore the old file name
                new_name = file.split("_")[1]
                new_name_path = os.path.join(path, new_name)
                os.rename(os.path.join(path, file), new_name_path)

                # write the zip file
                chroma_zip.write(new_name_path, arcname=new_name)

                # report that the file was zipped
                print("\tZipped", new_name_path)

    # return the filename of the zipped folder
    return chroma_file


if __name__ == "__main__":
    # make sure the user supplied command line arguments
    if len(sys.argv) != 2:
        print("Usage: ./processing.py <ChromaEffects file>")
        quit()

    # get the name of the ChromaEffects file from the command line and determine the extraction folder's name
    chroma_zip_file = sys.argv[1]
    extract_folder_name = chroma_zip_file + "_files"

    # extract the ChromaEffects file(s) to the extraction folder
    print("Extracting from", chroma_zip_file + "to" + extract_folder_name + ":")
    chroma_folder = unzip_chroma(chroma_zip_file, extract_folder_name)
    print("\n")

    # process the xml
    print("Process the XML:")

    chroma_files = os.listdir(chroma_folder)
    for chroma_file in chroma_files:
        print("Parsing", chroma_file + ":")
        parse_xml(chroma_folder + "\\" + chroma_file)

    print("\n")

    # zip the ChromaEffects files and get the resulting zip name
    chroma_zip_file_new = chroma_zip_file + "_new"

    print("Zipping", chroma_folder + " to " + chroma_zip_file_new + ":")
    new_chroma_zip_file = zip_chroma(chroma_folder, chroma_zip_file_new)
