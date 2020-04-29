
# Part 1: Introducing TensorFlow Datasets in YonoHub Suit — Image Classification with YonoHub &…



Over the past few years, researchers struggled to find suitable datasets that fit well in their applications. Recently, we were hit by a data storm which enriches our pockets with plenty of datasets which make the job done. However, such a storm has a double-sided effect as we consume a painful time writing different scripts to extract and manipulate these data.

On February 26, 2019, Tensorflow had announced [Tensorflow Datasets ](https://blog.tensorflow.org/2019/02/introducing-tensorflow-datasets.html)([GitHub](https://github.com/tensorflow/datase)) which as I quote,
> exposes public research datasets as [*tf.data.Datasets](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)* and as NumPy arrays. It does all the grungy work of fetching the source data and preparing it into a common format on disk, and it uses the [*tf.data API](https://www.tensorflow.org/guide/datasets)* to build high-performance input pipelines, which are TensorFlow 2.0-ready and can be used with *tf.keras* models.

Thus, we have a usable high-level layer we can use to call many datasets in a fast way. But can we do better? Can we have an extra layer that even remove the process of writing a line of code?

[YonoArc](https://yonohub.com/yonoarc/) in the [YonoHub](https://yonohub.com/) platform provides such a visual programming tool that you easily pick and play some pre-implemented blocks. Your task is to choose which dataset you prefer. But what is the YonoHub platform?
> Yonohub is the first cloud-based system for designing, sharing, and evaluating complex systems, such as Autonomous Vehicles, ADAS, and Robotics. Yonohub features a drag-and-drop tool to build complex systems consisting of many blocks, a marketplace to share and monetize blocks, a builder for custom environments, and much more.

In this series of tutorials, we will go through a deep learning journey, especially **Image Classification**, starting from streaming a dataset till the deployment. The tutorials cover how to use Tensorflow in YonoHub by using the blocks offered within YonoArc.

In this tutorial, we will see how to use the Tensorflow Datasets Player block (Image Classification category) within YonoArc. Covering the visualization of over 50 different image classification datasets streamed from a single block. We will use some utils blocks from the OpenCV package in YonoArc.

## Tensorflow Datasets in YonoArc

Just a few steps and you run your first pipeline of YonoArc blocks. First of all, you need to [signup](https://app.yonohub.com/) in YonoHub. After signing in, you will have some core Apps, in the Main View, which you can check them later one by one using the aid of the official [website](https://yonohub.com/).

![Main View](https://cdn-images-1.medium.com/max/2004/1*M88cYQCoIT2-JGAD0BhyeA.png)*Main View*

Let’s focus on YonoArc but first, you will need to freely purchase some necessary blocks. To do so you need to click on [YonoStore](https://yonohub.com/yonostore/),
> YonoStore is a marketplace for the state-of-the-art blocks, datasets, and ready-made runtime environments. YonoStore is fully accessible by both the online users and the users of any on-premises Yonohub, while still protecting everyone’s intellectual property.

Follow YonoStore [documentation](https://docs.yonohub.com/docs/yonohub/yonostore/) to purchase any product. For our tutorial, search for the following blocks,

* [Image Classification TFDS Player](https://store.yonohub.com/product/image-classification-player/)

* [OpenCV Draw Label](https://store.yonohub.com/product/draw-label/)

After purchasing, let’s create a pipeline!

### Visualize Tensorflow Datasets

In the next clip, we demonstrate how to create a pipeline and launch it. This pipeline aims to investigate the usage of the Image Classification TFDS Player by visualization various numbers of datasets for image classification.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/yspgvzk1Y8/0.jpg)](https://www.youtube.com/watch?time_continue=4&v=-yspgvzk1Y8&feature=emb_logo)

The clip shows the advantage of using YonoArc for datasets streaming. We visualized different datasets like beans and cifar10. Furthermore, the frame rate of the streaming has been changed in live mode. You do not need to terminate the full pipeline for that. But can we do more?

### Preprocess and Draw Labels

We need to interact with raw images as well as the labels by doing some preprocessing to prepare the training process for such a dataset. In the next clip, we illustrate how to create a custom block to simply resize the streamed images using *cv2.resize* function in python. Moreover, we draw the streamed labels on top of the resized image using the OpenCV Draw Label block we purchased early.

[![]()](https://youtu.be/XQAEguGxWrk)

Now you implement a full pipeline that streams, preprocesses, annotates, and visualizes the beans dataset. You implement a custom block to resize images.

To learn more about creating blocks in YonoArc, check the [docs](https://docs.yonohub.com/docs/yonohub/yonoarc/creating-yonoarc-blocks/). You can check the article’s pipeline as well as the source codes for all the blocks used in this [repository](https://github.com/YonoHub/Introducing-TensorFlow-Datasets-in-YonoHub-Suit.git). Furthermore, you can purchase the [OpenCV Resize](https://store.yonohub.com/product/resize/) block from YonoStore, it contains the same functionality as the one you implemented but with more features.

## Conclusion

Finally, you are ready to use the pipeline for training. In the next article, we will build a CNN model to classify the cifar10 dataset’s classes. The model will be implemented using Tensorflow V2.0 and encapsulated as a block in YonoArc. It’s easy to try out Yonohub. New users receive $25 free credits. Sign up on [Yonohub](https://yonohub.com/)!

## Reference

[1] [https://blog.tensorflow.org/2019/02/introducing-tensorflow-datasets.html](https://blog.tensorflow.org/2019/02/introducing-tensorflow-datasets.html)

[2] [https://www.tensorflow.org/datasets/catalog/overview](https://www.tensorflow.org/datasets/catalog/overview)

[3] [https://yonohub.com](https://yonohub.com/)

[4] [https://docs.yonohub.com](https://docs.yonohub.com/)










