<script setup lang="ts">
import { ref } from 'vue'
import { useMotion } from '@vueuse/motion'
import { uploadFile } from '@/utils/api'

const fileInput = ref<HTMLInputElement | null>(null)
const files = ref<File[]>([])
const status = ref<'idle' | 'success' | 'error' | 'uploading'>('idle')

function triggerInput() {
  fileInput.value?.click()
}

function handleChange(e: Event) {
  const fileList = (e.target as HTMLInputElement).files
  if (fileList && fileList[0]) {
    files.value = Array.from(fileList)
  }

  input.value = '';
}

async function upload() {
  if (!files.value.length) return
  status.value = 'uploading'
  const formData = new FormData()
  formData.append('file', files.value[0])
  formData.append('user_id', 'karna23')
  
  try {
    await uploadFile(files.value[0], 'karna23')
    status.value = 'success'
  } 
  catch (error) {
  let message = error?.message || 'Unknown error';
  console.log("Caught error:", message);

  if (message === "File is not syllabus content.") {
    status.value = 'invalid';
  } else {
    status.value = 'error';
  }
  fileInput.value!.value = '';
}
}
</script>

<template>
  <div class="upload-wrapper">
    <h1>📘 AI Study Planner</h1>
    <input type="file" @change="handleChange" />
    <p>Upload file</p>
    <p>Drag or drop your files here or click to upload</p>

    <div v-if="files.length">
      <p>Selected: {{ files[0].name }}</p>
      <p>Size: {{ (files[0].size / 1024 / 1024).toFixed(2) }} MB</p>
      <p>Type: {{ files[0].type }}</p>
      <p>Last Modified: {{ new Date(files[0].lastModified).toLocaleDateString() }}</p>
    </div>

    <div v-if="status === 'uploading'" class="status">Uploading...</div>
    <div v-if="status === 'success'" class="status success">✅ File uploaded successfully!</div>
    <div v-if="status === 'invalid'" class="status invalid">⚠️ This file doesn’t look like a valid syllabus. Please try again.</div>
    <div v-if="status === 'error'" class="status error">❌ Upload failed. Try again later.</div>

    <button @click.stop="upload">Upload</button>
  </div>
</template>

