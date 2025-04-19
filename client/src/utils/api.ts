export async function uploadFile(file: File, user_id: string) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("user_id", user_id);

  const response = await fetch("https://tutormeow-production.up.railway.app/upload", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) throw new Error("Upload failed");

  return response.json();
}
