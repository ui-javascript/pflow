<template>


  <Row :gutter="10">
    <Col :span="12">
      <Card title="阿里云图床配置">
        <p>
          <Input placeholder="请输入region" v-model.trim="region" />
        </p>
        <p>
          <Input placeholder="请输入accessKeyId" v-model.trim="accessKeyId" />
        </p>
        <p>
          <Input placeholder="请输入accessKeySecret" v-model.trim="accessKeySecret" />
        </p>
        <p>
          <Input placeholder="请输入bucket" v-model.trim="bucket" />
        </p>

        <Upload
            :disabled="!region || !accessKeyId || !accessKeySecret || !bucket"
            @change="onChange"
            draggable
            :show-file-list="false"
            :auto-upload="false" />

      </Card>

    </Col>

    <Col :span="12">
      <List>
        <template #header>今日上传记录
        </template>
        <ListItem v-for="item in list"><Link target="_blank" :href="item.url">{{item.name}}</Link></ListItem>
      </List>
    </Col>
  </Row>


</template>

<script setup>
import OSS from "ali-oss"
import {ref} from "vue"
import moment from "moment"

const uploadRef = ref();
const files = ref([]);

const list = ref([])

const region = ref(localStorage.getItem("region"))
const accessKeyId = ref(localStorage.getItem("accessKeyId"))
const accessKeySecret = ref(localStorage.getItem("accessKeySecret"))
const bucket = ref(localStorage.getItem("bucket"))

const getCustomIcon = () => {
  return {
    startIcon: () => false,
    removeIcon: () => false,
  };
};


const onChange = (fileList) => {
  // console.log(fileList)
  files.value = fileList;
  handleUpload(fileList[fileList.length - 1])
};

const initClient = () => {
  if (!region.value || !accessKeyId.value || !accessKeySecret.value || !bucket.value) {
    return false
  }
  localStorage.setItem("region", region.value)
  localStorage.setItem("accessKeyId", accessKeyId.value)
  localStorage.setItem("accessKeySecret", accessKeySecret.value)
  localStorage.setItem("bucket", bucket.value)

  return new OSS({
    region: region.value,
    accessKeyId: accessKeyId.value,
    accessKeySecret: accessKeySecret.value,
    bucket: bucket.value,
    secure: true,
  });
}

const randomStr = (len) => {
  len = len || 32;

  // 默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1
  const $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
  const maxPos = $chars.length;
  let pwd = '';
  for (let i = 0; i < len; i++) {
    pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
  }
  return pwd;
}

const handleUpload = async (file) => {
  // console.log(file)
  const client = initClient()
  if (!client) {
    return
  }
  await client.multipartUpload(moment(new Date()).format("YYYYMMDD-HHmmss") + "-" + randomStr(12) + "-" + file.name, file.file)
  listLatest()
}

const listLatest = async () => {
  const client = initClient()
  if (!client) {
    return
  }
  const res = await client.list({
    // 'max-keys': limit,
    'prefix': moment(new Date()).format("YYYYMMDD-")
  })

  list.value = res.objects.reverse()
}
listLatest()


</script>