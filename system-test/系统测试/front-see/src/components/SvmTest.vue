<template>
  <div class="contain2">
    <div class="putbutton">
      <input
        id="btn_file"
        type="file"
        @change="handleFileChange"
        style="display: none"
        accept="image/jpeg"
      />
      <button @click="handleSelectFile" class="my_button" id="uploadimg">
        上传图片
      </button>

      <button @click="handleButtonClick2" class="my_button" id="start">
        检测
      </button>
    </div>
    <div class="showimg">
      <div class="building">
        <!-- <div class="mybutton" @click="handleButtonClick2"></div> -->
        <img
          v-if="selectedFile"
          :src="previewUrl"
          alt="Selected Image"
          class="scaled-image"
        />
      </div>
      <div class="building">
        <img
          :src="imagePath"
          alt="Detected Image"
          class="scaled-image"
          v-if="imagePath"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { message } from "ant-design-vue";

const imagePath = ref(null);
const selectedFile = ref(null);

const uploadImage = async () => {
  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await axios.post("http://localhost:7078/svm", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    imagePath.value = `data:image/jpeg;base64,` + response.data.imageBase64;
    console.log(imagePath.value);
    //console.log(imagePath.value);
  } catch (error) {
    console.error("Error uploading image:", error);
  }
};

//选择图片的预览部分
const previewUrl = ref(null);

const handleFileChange = (event) => {
  selectedFile.value = event.target.files[0];

  if (!selectedFile.value) {
    // 如果未选择文件，则显示警告消息
    message.warning("No image selected");
  } else {
    // 如果选择了文件，则预览图片
    const reader = new FileReader();

    reader.onload = () => {
      previewUrl.value = reader.result;
    };

    reader.readAsDataURL(selectedFile.value);
  }
};

//按钮

const handleButtonClick2 = () => {
  if (selectedFile.value) {
    uploadImage();
  } else {
    message.warning("image is empty");
  }
};

function handleSelectFile() {
  document.getElementById("btn_file").click();
}
</script>

<style scoped>
.contain2 {
  width: 70%;
  height: 90%;
  position: fixed;
  display: flex;
  flex-direction: column;
  top: 1%; /* 向下移动 20px */
  right: 8%; /* 向左移动 20px */
}

.putbutton {
  /* background-color: #000; */
  margin-top: 3px;
  padding-left: 70%;
}
.showimg {
  /* background-color: aqua; */
  display: flex;
  flex-direction: row;
}
.building {
  background-color: rgba(255, 255, 255, 0.85);
  border: 1px solid #000; /* 黑色边框 */

  padding: 10px; /* 内边距，使内容不贴紧边框 */

  /* margin: 200px auto; */
  margin: 12% 0 0 10%;
  width: 450px;
  height: 400px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}

.scaled-image {
  max-width: 100%; /* 设置最大宽度为父元素宽度 */
  max-height: 100%; /* 设置最大高度为父元素高度 */
  object-fit: contain; /* 保持图像的纵横比，完全适应元素框，可能会在父元素内留有空白 */
  padding: 0px;
  object-position: center center; /* 图像在其容器中垂直和水平居中 */
}

.my_button {
  color: #333333;
  background-color: #fff;
  padding: 10px 30px;
  margin-right: 10%;
  outline: none;
  border: 1px solid #ccc;
}

.my_button:hover {
  background-color: rgb(10, 150, 139); /* 将悬停背景颜色设为蓝色 */
  cursor: pointer; /* 将鼠标指针形状设置为手形 */
}
</style>
