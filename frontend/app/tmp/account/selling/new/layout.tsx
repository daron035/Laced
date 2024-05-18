interface Props {
  children: React.ReactNode;
}

export default function Layout({ children }: Props) {
  return <div className="max-w-3xl mx-auto py-12 px-10">{children}</div>;
}
