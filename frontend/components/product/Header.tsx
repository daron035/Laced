type Props = {
    brand: string;
    sku: string;
    name: string;
  };
  
  export default function Header({ brand, sku, name }: Props) {
    return (
      <div className="pb-8">
        <div className="mb-2 text-[14px] leading-none">
          {brand} / {sku}
        </div>
        <div className="text-[#101010]">
          <h1 className="text-[28px] leading-none">{name}</h1>
        </div>
      </div>
    );
  }
  