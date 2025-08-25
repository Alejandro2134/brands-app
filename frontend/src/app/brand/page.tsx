"use client";

import { useState } from "react";
import BrandOperations from "../components/BrandOperations/BrandOperations";
import { useRouter } from "next/navigation";

const CreateBrand = () => {
  const router = useRouter();
  const [form, setForm] = useState({
    name: "",
    owner: "",
  });

  const createBrand = async () => {
    await fetch("https://brands-app.onrender.com/brand/", {
      method: "POST",
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
      formButtonText="Guardar Marca"
      formName="Registrar Marca"
      handleSubmit={handleSubmit}
      form={form}
      handleChange={handleChange}
    />
  );
};

export default CreateBrand;
