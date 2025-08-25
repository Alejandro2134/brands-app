"use client";

import { useRouter } from "next/navigation";
import BrandOperations from "../../components/BrandOperations/BrandOperations";

import { use, useState } from "react";

const UpdateBrand = ({ params }: { params: Promise<{ id: string }> }) => {
  const { id } = use(params);
  const router = useRouter();
  const [form, setForm] = useState({
    name: "",
    owner: "",
  });

  const createBrand = async () => {
    await fetch(`https://brands-app.onrender.com/brand/${id}/`, {
      method: "PUT",
      body: JSON.stringify(form),
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createBrand();
    router.push(`/panel`);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <BrandOperations
      formButtonText="Actualizar Marca"
      formName="Actualizar Marca"
      handleSubmit={handleSubmit}
      form={form}
      handleChange={handleChange}
    />
  );
};

export default UpdateBrand;
