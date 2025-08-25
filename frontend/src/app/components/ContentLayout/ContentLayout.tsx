type ContentLayoutProps = {
  contentTitle: string;
  children: React.ReactNode;
};

const ContentLayout: React.FC<ContentLayoutProps> = ({
  contentTitle,
  children,
}) => {
  return (
    <div className="flex flex-col flex-1 overflow-hidden">
      <div className="p-3 mb-10 rounded-2xl bg-red-400">
        <h1 className="text-3xl font-bold">{contentTitle}</h1>
      </div>

      {children}
    </div>
  );
};

export default ContentLayout;
