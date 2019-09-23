import os

################################################################################
############################### Functions ######################################

def recursiveReplace(my_base_dir,o,c):
	folder_list = os.listdir(my_base_dir)

	for item in folder_list:
		new_name = item.replace(o, c)
		if o in item:
			new_name = item.replace(o, c)
			os.rename(os.path.join(my_base_dir,item), os.path.join(my_base_dir, new_name))
		if os.path.isdir(os.path.join(my_base_dir, new_name)):
			recursiveReplace(os.path.join(my_base_dir, new_name), o, c)

################################################################################
print('Enter file directory to start search from: ')
my_base_dir = str(input())
print('Enter character to remove: ')
char_to_remove = str(input())
print('Enter character to replace with:')
char_to_replace  = str(input())
recursiveReplace(my_base_dir, str(char_to_remove), str(char_to_replace))
print('Replaced all instances of ' + char_to_remove + ' with ' + char_to_replace)
print('END')

