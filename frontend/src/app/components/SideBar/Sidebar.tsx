"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const Sidebar = () => {
  const pathname = usePathname();

  return (
    <div className="w-60 p-3 border-1 border-red-400">
      <div className="pb-7 flex justify-center">
        <h1 className="text-3xl text-red-400">Marcas App</h1>
      </div>

      <div>
        <h2 className="font-light text-[#a0a0a0] text-2xl">Dashboard</h2>
        <Link href="/panel">
          <div
            className={`flex pl-3 h-9 items-center rounded-2xl ${
              pathname === "/panel" ? "bg-red-400" : "hover:bg-red-400"
            } `}
          >
            <h3 className="flex-1 font-bold">Panel</h3>
          </div>
        </Link>
      </div>

      <div>
        <h2 className="font-light text-[#a0a0a0] text-2xl">Services</h2>
        <Link href="/brand">
          <div
            className={`flex pl-3 h-9 items-center rounded-2xl ${
              pathname === "/brand" ? "bg-red-400" : "hover:bg-red-400"
            } `}
          >
            <h3 className="flex-1 font-bold">Registro de Marca</h3>
          </div>
        </Link>
      </div>
    </div>
  );
};

export default Sidebar;
