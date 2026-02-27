# windows_AMD显卡ai 

>ヾ(≧▽≦*)oヾ(≧▽≦*)oヾ(≧▽≦*)oヾ(≧▽≦*)oヾ(≧▽≦*)o

由于光追性能和CUDA的差距，相近光栅性能的A卡和N卡在游戏性能差不多的情况下，价格有一两千的差距。对于游戏玩家而言，性价比更高的A卡是更好的选择。但是，如果想用A卡来玩一些生产力相关AI方面的东西，那该怎么办呢？

这篇文章也许会对你有所帮助。

> 需要：miniconda（虚拟环境）python AMD 显卡 7000系及以上

1. 找一个大点的地方，创建一个文件夹（最好路径上没有中文）
2. win+r  cmd 或者在微软商店下载 powershell （win11好像自带，win+q 搜一下看看？）

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210164857993.png" alt="image-20251210164857993" />

3. cmd 进入 你创建的文件夹

   ```
   conda create --name comfy python=3.12 
   ```

   创建一个名字是 comfyui-amd 的虚拟环境（名字随意）（注意后面的Python版本，选择你需要的）

   可能会有报错，有可能是conda没有在环境变量里，添加后就行。（powershell 可能会有个人系统配置的要求，报错的代码问ai最方便）

   ```
   conda env list # 展示你创建的虚拟环境（复制的时候把注释去掉）
   ```

   ```
   conda activate comfy #进入虚拟环境
   ```

   <img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170100959.png" alt="image-20251210170100959" />

   

> 使用powershell也行，更现代集成更多unix终端指令，类似这个：
>
> <img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210165434889.png" alt="image-20251210165434889" />

4. 浏览器输入https://github.com/comfyanonymous/ComfyUI （comfyui的github库），右边releases里选择amd的包。

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210165214335.png" alt="image-20251210165214335" />

5. 下载下来的包解压在你创建的文件夹里。

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210165256142.png" alt="image-20251210165256142" />

6. 下载下来的文件里有个README_VERY_IMPORTANT.txt的文件，是作者的教程。

   <img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210165701191.png" alt="image-20251210165701191" />

8. 需要安装amd的驱动https://www.amd.com/en/resources/support-articles/release-notes/RN-AMDGPU-WINDOWS-PYTORCH-7-1-1.html

   ​	在这个页面点击这个连接<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210165757944.png" alt="image-20251210165757944" />

   https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/windows/install-pytorch.html

   <img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210165835151.png" />

   是amd 官方的rocm blog

   

9. 在cmd 或者powershell 你打开的文件夹里使用命令：

   ```
   cd .\ComfyUI_windows_portable\
   cd .\ComfyUI\ # 进入文件夹
   ```

10. 按照amd 的官方教程 

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170457098.png" alt="image-20251210170457098" />

输入相应的命令，并验证安装的pytorch

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170512336.png" alt="image-20251210170512336" />

11. 有一个细节需要注意!<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170633488.png" alt="image-20251210170633488" />

这里显示的显卡可能是你的核显，修改数字后才是你的独立显卡，例如：

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170757968.png" alt="image-20251210170757968" />

我的是device[1]

12. 下载并验证成功后，在<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170909957.png" alt="image-20251210170909957" />

这个路径，输入

```
pip install -r requirements.txt 
```

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210170947067.png" alt="image-20251210170947067" />

就是下载文件夹里的这个文件里所需的依赖。

13. 全部完成之后，<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171034904.png" alt="image-20251210171034904" />

在这个文件夹里有一个run_amd_gpu.bat文件，也可以使用run_amd_gpu_disable_smart_memory.bat这个。

> 后面这个在作者的提示里：If you have memory issues you can try disabling the smart memory management by running comfyui with:
>
> run_amd_gpu_disable_smart_memory.bat

> 翻译之后就是：如果您遇到内存问题，您可以尝试通过运行 comfyui 来禁用智能内存管理：
> 	run_amd_gpu_disable_smart_memory.bat

> 按你的需要选择（或者其中一个错误之后换一个）

右键编辑，添加<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171416083.png" alt="image-20251210171416083" />

```
--cuda-device 1 #因为我的独显的编号是1,你选你自己的，用哪个启动就改哪个
```

14.



<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171601375.png" alt="image-20251210171601375" />

```
cd ..
```



退回到上一级目录

```
.\run_amd_gpu_disable_smart_memory.bat
```

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171702816.png" alt="image-20251210171702816" />

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171737142.png" alt="image-20251210171737142" />

会自动跳出来个web页面（有问题的把上面的命令行复制给ai纠错）

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171827281.png" alt="image-20251210171827281" />

15. 关掉页面

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210171905514.png" alt="image-20251210171905514" />

在这个路径下把你的模型放进去（或者使用作者提供的修改文件的方法，映射你的模型路径）

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172005089.png" alt="image-20251210172005089" />

16. 

 

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172121429.png" alt="image-20251210172121429" />

关掉所有的工作流，会出来一个默认的。

在这里选择模型，

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172141477.png" alt="image-20251210172141477" />

在这两个地方修改提示词

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172302781.png" alt="image-20251210172302781" />

这里修改图片的像素

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172316571.png" alt="image-20251210172316571" />



这里修改生成步数等

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172337397.png" alt="image-20251210172337397" />

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172344686.png" alt="image-20251210172344686" />

出图

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172414162.png" alt="image-20251210172414162" />

powershell 显示

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172419130.png" alt="image-20251210172419130" />

出来的文件在这个路径

<img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172507167.png" alt="image-20251210172507167" />

17. 我是用的模型：https://civitai.com/models/376130/nova-anime-xl（科学上网）

18. ctrl + C 退出

    <img src="C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20251210172628623.png" alt="image-20251210172628623" />

再输入Y +回车

