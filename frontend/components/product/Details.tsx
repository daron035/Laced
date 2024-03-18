const Description = () => {
  return (
    <div className="mb-8">
      <h4 className="mb-2 text-[18px] text-[#101010]">Description</h4>
      <div className="mb-4 leading-normal">
        Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit
        enim labore culpa sint ad nisi Lorem pariatur mollit ex esse
        exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit
        nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor
        minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure
        elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor
        Lorem duis laboris cupidatat officia voluptate. Culpa proident
        adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod.
        Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim.
        Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa
        et culpa duis.
      </div>
    </div>
  );
};
export default function Details() {
  const details = ["Brand", "Categories", "Year realesed", "Colour"];

  return (
    <>
      <Description />
      <div>
        <h4 className="mb-2 text-[18px] text-[#101010]">Details</h4>
        <div className="divide-y">
          {details.map((name) => {
            return (
              <dl className="py-4 flex gap-x-2 text-[14px]">
                <dt>{name}</dt>
                <dd className="ml-auto text-[#101010]">Nike</dd>
              </dl>
            );
          })}
        </div>
      </div>
    </>
  );
}
