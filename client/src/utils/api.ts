// src/utils/api.ts

export async function uploadFile(file: File, user_id: string) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("user_id", user_id);

  const response = await fetch("https://tutormeow-production.up.railway.app/upload", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    console.log("this is the error - "+errorData);
    const message = errorData?.error || "Upload failed";
    throw new Error(message);
  }

  return await response.json();
}
