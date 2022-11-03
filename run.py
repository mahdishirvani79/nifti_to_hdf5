import h5py
import os
import shutil
import nibabel as nib

data_dir = "./nifti_data/datas/"
mask_dir = "./nifti_data/masks"


class getDataMask:
    def __init__(self, data_files:list, mask_files:list):
        self.data_files = data_files
        self.mask_files = mask_files

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data_files) > 0:
            data_file = self.data_files.pop(0)
            mask = self.match(data_file)
            return (mask, data_file)
        else:
            raise StopIteration


    #edit this method if your matching is diffrent
    #in my example data name is {NAME}_flair.nii and mask is {NAME}_mask.nii
    def match(self, data_file):
        data_file = data_file.replace("flair.nii", "")
        masks_list = [(i, s) for i, s in enumerate(self.mask_files) if data_file in s]
        i, mask = masks_list[0]
        self.mask_files.pop(i)
        return mask



def run():
    data_files = os.listdir(data_dir)
    mask_files = os.listdir(mask_dir)
    if os.path.exists("./h5data"):
        shutil.rmtree("./h5data")
    os.mkdir("./h5data")
    data_mask = getDataMask(data_files, mask_files)
    iterator = iter(data_mask)
    for mask, data in iterator:
        data_object = nib.load(data_dir + "/" + data).get_fdata()
        mask_object = nib.load(mask_dir + "/" + mask).get_fdata()
        name = data.replace("_flair.nii", ".h5")
        name = "./h5data/" + name
        with h5py.File(name, "w") as f:
            f.create_dataset("raw", data=data_object)
            f.create_dataset("label", data=mask_object)
        
    

if __name__ == "__main__":
    run()