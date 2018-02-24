# **车道线检测** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />

简介
---

当我们开车的时候，我们纯靠眼睛决定我们往哪开，我们可以根据道路上的直线判断车相对位置和角度。因此我们开发无人车的第一件事就是用图像处理算法自动检测车道线。

在这个项目中你将使用 Python 和 OpenCV 检测图像中的直线。 OpenCV全称是“Open-Source Computer Vision”，意思是开源计算机视觉库，它是一个包含许多有许多图像处理工具的软件包。

要完成该项目，你需要提交两个文件：一个项目代码的文件和一个简短的项目报告的文件，你需要在报告详细中介绍你的解决方案。我们已经包含了用于代码和报告的模板文件。代码文件是 [P1.ipynb](P1.ipynb)，报告模板是 [writeup_template.md](writeup_template.md)。

通过项目需要满足该项目的每一条[项目要求](https://review.udacity.com/#!/rubrics/322/view)。

如何写好思路报告
---
在本项目中，要写好报告就应该详细地写好反思部分，反思有三个部分：

1. 描述整个算法处理的流程

2. 报告算法可能存在的问题

3. 提出可行的改进方案

最好在描述处理流程的时候配图，会更有助于你对算法的理解。

写得要尽可能简洁，因为我们不是要写书，是要写一个简单的报告。

你不一定需要用 markdown 写，比如 word 或者其他的软件，只需要提交一个 pdf 文件或 markdown 文件。你可以参考这个报告模板： [writeup_template.md](writeup_template.md)。

项目
---

## 如果你已经安装了[CarND Term1 Starter Kit](https://github.com/nd013/CarND-Term1-Starter-Kit)，做这个项目会很方便！如果没有安装，你应该去安装。

**第一步：** 安装 [CarND Term1 Starter Kit](https://github.com/nd013/CarND-Term1-Starter-Kit)。如果你已经安装了，可以跳过这一步。课程链接：[CarND Term1 Starter Kit](https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/83ec35ee-1e02-48a5-bdb7-d244bd47c2dc/lessons/8c82408b-a217-4d09-b81d-1bda4c6380ef/concepts/4f1870e0-3849-43e4-b670-12e6f2d4b7a7)。

**第二步：** 在 Jupyter Notebook 中打开代码。

你需要在 Jupyter Notebook 中完成代码，如果你不熟悉 Jupyter Notebook，可以看这个入门教程：[Cyrille Rossant's Basics of Jupyter Notebook and Python](https://www.packtpub.com/books/content/basics-jupyter-notebook-and-python) 。

Jupyter 就是之前的 IPython Notebook，你可以交互式地运行代码块并查看结果。本项目的所有代码都包含在 Jupyter Notebook 中。 要在浏览器中启动 Jupyter，请先在终端中切换到项目目录（cd 命令），然后在终端提示符下运行以下命令（请确保已按照 [CarND Term1 Starter Kit](https://github.com/nd013/CarND-Term1-Starter-Kit) 入门工具包安装说明中所述激活了 Python 3 carnd-term1 环境。）：

`jupyter notebook`

执行上面的命令以后，会自动打开一个浏览器页面，里面会显示当前目录的文件，请点击 `P1.ipynb` ，然后会打开另一个页面，请按照 notebook 中的指示完成该项目。

**第三步：** 完成项目并提交 notebook 文件和项目报告。

## 如何编写 README 文件

写好 README 可以提升你的 GitHub 项目的吸引力，如果你想学习如何更好地写 README 文件，你可以学习这个免费课程：[编写 README 文档](https://www.udacity.com/course/writing-readmes--ud777)。


