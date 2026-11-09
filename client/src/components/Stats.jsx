function Stats() {
  const stats = [
    {
      number: "10K+",
      label: "Resumes Analysed",
    },
    {
      number: "95%",
      label: "ATS Accuracy",
    },
    {
      number: "5000+",
      label: "Happy Users",
    },
    {
      number: "24/7",
      label: "AI Available",
    },
  ];

  return (
    <section className="bg-slate-950 py-20">
      <div className="max-w-7xl mx-auto px-6">

        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">

          {stats.map((item, index) => (
            <div
              key={index}
              className="text-center"
            >
              <h2 className="text-5xl font-bold text-cyan-400">
                {item.number}
              </h2>

              <p className="text-slate-400 mt-3">
                {item.label}
              </p>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
}

export default Stats;