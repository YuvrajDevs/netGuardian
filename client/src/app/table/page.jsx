import DeviceReport from '@/components/DeviceReport'
import Severity from '@/components/Severity'
import Welcome from '@/components/Welcome'
import React from 'react'

const Table = () => {
  return (
    <div className='flex flex-col gap-y-6'>
      <Welcome />
      <DeviceReport />
      <Severity />
    </div>
  )
}

export default Table
