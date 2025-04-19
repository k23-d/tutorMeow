<template>
  <div class="upload-box">
    <label class="upload-label">
      <input type="file" @change="handleFileUpload" accept=".pdf,.doc,.docx" hidden />
      <span>Select your syllabus 📄</span>
    </label>

    <div v-if="selectedFile" class="file-preview">
      <p><strong>Uploaded:</strong> {{ selectedFile.name }}</p>
      <button @click="submitFile" :disabled="uploading">
        {{ uploading ? "Uploading..." : "Submit" }}
      </button>
    </div>

    <div v-if="successMessage" class="success">
      ✅ {{ successMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedFile = ref(null)
const uploading = ref(false)
const successMessage = ref("")

const userId = "demo_user_123" // 🔐 Replace with real user_id if using auth

function handleFileUpload(event) {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    successMessage.value = ""
  }
}

async function submitFile() {
  if (!selectedFile.value) return
  uploading.value = true

  const formData = new FormData()
  formData.append("file", selectedFile.value)
  formData.append("user_id", userId)

  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/upload`, {
      method: "POST",
      body: formData
    })

    const result = await response.json()
    successMessage.value = `File uploaded to ${result.path}`
  } catch (err) {
    console.error("Upload failed:", err)
    successMessage.value = "❌ Upload failed. Try again."
  } finally {
    uploading.value = false
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
.success {
  margin-top: 1rem;
  color: green;
}
</style>
