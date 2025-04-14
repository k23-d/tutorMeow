<template>
  <div class="upload-box">
    <label class="upload-label">
      <input type="file" @change="handleFileUpload" accept=".pdf,.doc,.docx" hidden />
      <span>Select your syllabus 📄</span>
    </label>

    <div v-if="selectedFile" class="file-preview">
      <p><strong>Uploaded:</strong> {{ selectedFile.name }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedFile = ref(null)

function handleFileUpload(event) {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    console.log('Selected file:', file.name)
    // TODO: send file to Supabase or backend
  }
}
</script>

<style scoped>
.upload-box {
  margin-top: 2rem;
  padding: 1.5rem;
  border: 2px dashed #aaa;
  border-radius: 10px;
  background-color: #f9f9f9;
}
.upload-label {
  display: inline-block;
  cursor: pointer;
  font-size: 1.1rem;
  color: #2a7de1;
}
.file-preview {
  margin-top: 1rem;
}
</style>
