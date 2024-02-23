"use client"
import Link from "next/link";

const DeviceReport = ({ deviceName, riskColor, reportUrl }) => {
  const downloadPdf = (url) => {
    const link = document.createElement('a');
    link.href = url;
    link.download = 'report.pdf';
    link.click();
  };

  return (
    <div className='bg-white flex rounded-xl mx-5 pt-5 pb-5 gap-x-10 justify-around'>
      <div className="flex flex-col items-center">
        <h1 className='font-outfit font-bold text-[24px] bg-yellow-400 px-4 py-1 rounded-full'>Device Name</h1>
        <h2 className='subHead'>Device 1</h2>
        <h2 className='subHead'>Device 2</h2>
        <h2 className='subHead'>Device 3</h2>
        <h2 className='subHead'>Device 4</h2>
        <h2 className='subHead'>Device 5</h2>
        <h2 className='subHead'>Device 6</h2>
      </div>
      <div className=" flex flex-col items-center">
        <h1 className='font-outfit font-bold text-[24px] bg-yellow-400 px-4 py-1 rounded-full'>Risk</h1>
        <div style={{ backgroundColor: "#62df00" }} className="tablelol riskBar w-16 color px-14 py-4 rounded-full"><span className="riskBarText">Low Risk</span> </div>
        <div style={{ backgroundColor: "#62df00" }} className="tablelol riskBar w-16 color px-14 py-4 rounded-full"></div>
        <div style={{ backgroundColor: "#ffff00" }} className="tablelol riskBar w-16 color px-14 py-4 rounded-full"></div>
        <div style={{ backgroundColor: "#62df00" }} className="tablelol riskBar w-16 color px-14 py-4 rounded-full"></div>
        <div style={{ backgroundColor: "#ffff00" }} className="tablelol riskBar w-16 mt-10 color px-14 py-4 rounded-full"></div>
        <div style={{ backgroundColor: "#ff0000" }} className="tablelol riskBar w-16 mt-7 color px-14 py-4 rounded-full"></div>
      </div>
      <div className="flex flex-col items-center">
        <h1 className='font-outfit font-bold text-[24px] bg-yellow-400 px-4 py-1 rounded-full'>Report URL</h1>
        <h2 className='cursor-pointer subHead text-gray-700 hover:text-black' onClick={() => downloadPdf(reportUrl)}>Download Report</h2>
        <h2 className='cursor-pointer subHead text-gray-700 hover:text-black' onClick={() => downloadPdf(reportUrl)}>Download Report</h2>
        <h2 className='cursor-pointer subHead text-gray-700 hover:text-black' onClick={() => downloadPdf(reportUrl)}>Download Report</h2>
        <h2 className='cursor-pointer subHead text-gray-700 hover:text-black' onClick={() => downloadPdf(reportUrl)}>Download Report</h2>
        <h2 className='cursor-pointer subHead text-gray-700 hover:text-black' onClick={() => downloadPdf(reportUrl)}>Download Report</h2>
        <h2 className='cursor-pointer subHead text-gray-700 hover:text-black' onClick={() => downloadPdf(reportUrl)}>Download Report</h2>
      </div>
      <div className="flex flex-col items-center">
        <h1 className='font-outfit font-bold text-[24px] bg-yellow-400 px-4 py-1 rounded-full'>Report Generated Time</h1>
        <h2 className='subHead'>Timestamp</h2>
        <h2 className='subHead'>Timestamp</h2>
        <h2 className='subHead'>Timestamp</h2>
        <h2 className='subHead'>Timestamp</h2>
        <h2 className='subHead'>Timestamp</h2>
        <h2 className='subHead'>Timestamp</h2>
      </div>
    </div>
  );
};

export default DeviceReport;
