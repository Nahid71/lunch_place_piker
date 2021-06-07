import os
import argparse


def check_backend_services(user_txt):
    if "arik" == user_txt: # only for this user
        try:
            # PATH TO THE BATCH FILE
            os.system(r"C:\Users\arik\Desktop\services_batch\backend_services.bat")
            return True
        except:
            print("Services were not started!")
    else:
        return False


def remove_migration_files(windows=True, setup_db=False):
    if setup_db:
        check_backend_services(os.getlogin())
    else:
        pass
    try:
        if windows == True:
            for root, dirs, files in os.walk(".", topdown=False):
                for name in dirs:
                    if name == "migrations":
                        migrations_dir = os.path.join(root, name)
                        for r, d, f in os.walk(migrations_dir):
                            for n in f:
                                file_name = os.path.join(r, n)
                                if "__init__.py" in file_name:
                                    continue
                                else:
                                    os.remove(file_name)
    except:
        return False
    return True


ap = argparse.ArgumentParser()

# Add the arguments
ap.add_argument("-d", "--setupdatabase", type=str, default="no", help="setup database")
args = vars(ap.parse_args())

# process only for windows
remove_migration_files(os.name == 'nt', args["setupdatabase"].lower() in ['yes', 'y', 'true'])
