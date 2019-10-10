<img align="center" src="./assets/logo.png" />

### **Better Backup Strategy For Your Youtube Videos.**

Python script to make JSON directory tree and downloading Youtube videos inside that folder automatically.

## :information_source: What Does it Do?
YTBackup is an efficient backup technique for your youtube video folders.
let say you have tons of youtube videos which you downloaded from any online YouTube video downloaders like ``ssyoutube``, ``9xyoutube`` etc etc. and you want to make a backup for it. so YTBackup will automatically create a JSON (Javascript Object Notation) file containing all the videos you have in the folder with their respective titles, and resolution like this ``{["videos\\myvideotitle.mp4", 720]}``.

YTBackup Restores all the videos as the same folder structure previously have which is a great thing about it.



----------

## :floppy_disk: Get Started

* clone this repo by typing this command in terminal

```bash
git clone https://github.com/askbuddie/YTBackup.git
```

* you also have to install the dependencies for running YTBackup by running

```bash
pip install -r requirements.txt
```

* when you have the **YTbackup.py** file. simply run the .py file in terminal and you will be prompted to add some info about the file path / folder path. just follow the steps

```bash
>> D:\CAM Files\Python\OS>YTBackup.py --backup
```

now YTBackup.py expects an arguments to be passed which defines what proccess you are doing, **restore** or **backup**.

> if you wanna do backup use **--backup**

> and if you wanna restore use **--restore** 

now once you do --backup you can save the json file in some other place safe, and by doing --restore you can also restore the videos.

----------

## :heart: Contribution
You wanna contribute to the project? Great to hear that.

please refer to our Contribution Guide [here](./CONTRIBUTING.md)

-----------

## :octocat: Author

- **Ask Buddie**

-----------

Thanks to [Ashish](https://github.com/ashiishme) for giving me an opportunity to contribute on AskBuddie

:heart: AskBuddie
