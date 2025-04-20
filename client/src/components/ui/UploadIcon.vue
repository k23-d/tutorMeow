<!-- components/ui/UploadIcon.vue -->
<template>
  <motion.div
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1, y: 0 }"
    :leave="{ opacity: 0, y: -10 }"
    class="text-neutral-600 dark:text-neutral-400"
  >
    <IconUpload class="w-6 h-6" />
  </motion.div>
</template>

<script setup lang="ts">
import { IconUpload } from '@tabler/icons-vue'
import { useMotion } from '@vueuse/motion'
</script>
