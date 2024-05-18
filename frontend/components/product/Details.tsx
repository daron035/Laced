const Description = ({ data }: { data: string }) => {
  return (
    <div className="mb-8">
      <h4 className="mb-2 text-[18px] text-[#101010]">Description</h4>
      <div className="mb-4 leading-normal">{data}</div>
    </div>
  );
};

type Props = {
  brand: string;
  categories: string[];
  description: string;
  year_released: string;
  colour: string;
};

export default function Details({
  brand,
  categories,
  description,
  year_released,
  colour,
}: Props) {
  const detail = [
    { Brand: brand },
    { Categories: categories?.join(", ") },
    { "Year realesed": year_released },
    { Colour: colour },
  ];

  return (
    <>
      <Description data={description} />
      <div>
        <h4 className="mb-2 text-[18px] text-[#101010]">Details</h4>
        <div className="divide-y">
          {detail.map((item, index) => {
            const [key, value] = Object.entries(item)[0];
            if (!value) return null;
            return (
              <dl key={index} className="py-4 flex gap-x-2 text-[14px]">
                <dt>{key}</dt>
                <dd className="ml-auto text-[#101010]">{value}</dd>
              </dl>
            );
          })}
        </div>
      </div>
    </>
  );
}
