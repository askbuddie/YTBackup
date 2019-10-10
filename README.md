<img align="center" src="./assets/logo.png" />
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors)

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="http://anuraghazra.github.io"><img src="https://avatars3.githubusercontent.com/u/35374649?v=4" width="100px;" alt="Anurag Hazra"/><br /><sub><b>Anurag Hazra</b></sub></a><br /><a href="https://github.com/askbuddie/YTBackup/commits?author=anuraghazra" title="Code">💻</a> <a href="https://github.com/askbuddie/YTBackup/commits?author=anuraghazra" title="Documentation">📖</a> <a href="#design-anuraghazra" title="Design">🎨</a> <a href="#ideas-anuraghazra" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-anuraghazra" title="Maintenance">🚧</a> <a href="#tool-anuraghazra" title="Tools">🔧</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!