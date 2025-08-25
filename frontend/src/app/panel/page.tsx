"use client";

import ContentLayout from "@/app/components/ContentLayout/ContentLayout";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { Brand } from "../types/Brand";

const Panel = () => {
  const router = useRouter();
  const [brands, setBrands] = useState<Brand[]>([]);
  const [refresh, setRefresh] = useState(false);

  const handleDeleteButton = async (id: string) => {
    await fetch(`https://brands-app.onrender.com/brand/${id}`, {
      method: "DELETE",
    });

    setRefresh((prev) => !prev);
  };

  const handleUpdateButton = (brandId: string) => {
    router.push(`/brand/${brandId}`);
  };

  useEffect(() => {
    fetch("https://brands-app.onrender.com/brand/")
      .then((res) => res.json())
      .then((data) => {
        setBrands(data);
      });
  }, [refresh]);

  return (
    <ContentLayout contentTitle="Dashboard/Panel">
      <div className="flex flex-col flex-1 overflow-hidden">
        <div className="flex-1 overflow-auto border border-red-400 p-3 rounded-2xl">
          <table className="w-full border-collapse">
            <thead className="sticky top-0 bg-white z-10 shadow">
              <tr>
                <th className="text-center align-middle px-4 py-2"></th>
                <th className="text-center align-middle px-4 py-2">Marca</th>
                <th className="text-center align-middle px-4 py-2">Titular</th>
                <th className="text-center align-middle px-4 py-2">Estado</th>
                <th className="text-center align-middle px-4 py-2">Acciones</th>
              </tr>
            </thead>
            <tbody>
              {brands.map((brand, index) => (
                <tr key={brand.id}>
                  <td className="text-center align-middle px-4 py-2">
                    {index + 1}
                  </td>
                  <td className="text-center align-middle px-4 py-2">
                    {brand.name}
                  </td>
                  <td className="text-center align-middle px-4 py-2">
                    {brand.owner}
                  </td>
                  <td className="text-center align-middle px-4 py-2">
                    {brand.status ? "Activo" : "No activo"}
                  </td>
                  <td className="text-center align-middle px-4 py-2">
                    <div>
                      <button
                        onClick={() => handleDeleteButton(brand.id)}
                        className="text-red-600 cursor-pointer"
                      >
                        Eliminar
                      </button>
                      <button
                        onClick={() => handleUpdateButton(brand.id)}
                        className="text-green-600 cursor-pointer"
                      >
                        Actualizar
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </ContentLayout>
  );
};

export default Panel;
