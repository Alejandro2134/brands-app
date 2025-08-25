"use client";

import ContentLayout from "../ContentLayout/ContentLayout";

type BrandOperationsProps = {
  formName: string;
  handleSubmit: (e: React.FormEvent) => void;
  formButtonText: string;
  handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  form: { name: string; owner: string };
};

const BrandOperations: React.FC<BrandOperationsProps> = ({
  formName,
  handleSubmit,
  formButtonText,
  form,
  handleChange,
}) => {
  return (
    <ContentLayout contentTitle="Servicios/Registrar Marca">
      <form
        onSubmit={handleSubmit}
        className="max-w-md mx-auto bg-white p-6 rounded-2xl shadow-lg space-y-5"
      >
        <h2 className="text-3xl text-red-400 font-bold text-center mb-4">
          {formName}
        </h2>

        <div className="space-y-2">
          <label className="text-gray-700 font-semibold block">
            Nombre de la marca
          </label>
          <input
            name="name"
            value={form.name}
            onChange={handleChange}
            className="w-full border rounded-xl p-2 outline-none focus:ring-2 focus:ring-red-400"
            placeholder="Ej. Coca Cola"
          />
        </div>

        <div className="space-y-2">
          <label className="text-gray-700 font-semibold block">Titular</label>
          <input
            name="owner"
            value={form.owner}
            onChange={handleChange}
            className="w-full border rounded-xl p-2 outline-none focus:ring-2 focus:ring-red-400"
            placeholder="Nombre del titular"
          />
        </div>

        <div className="text-center">
          <button
            type="submit"
            className="bg-red-400 hover:bg-red-500 transition-color font-semibold py-2 px-6 rounded-xl"
          >
            {formButtonText}
          </button>
        </div>
      </form>
    </ContentLayout>
  );
};

export default BrandOperations;
