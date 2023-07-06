import React, { useState, useEffect } from 'react'

const Sse = () => {
    const [data, setData] = useState()
    useEffect(() => {
        const sse = new EventSource('http://localhost:5000/listen')
        sse.onmessage = e => {
            console.log(`Got msg: ${e.data}`)
            setData(e.data)
        }

        sse.onerror = e => {
            console.log(`Got err: ${e}`)
            console.log(e)

            sse.close();
        }
        return () => {
            sse.close();
        };
    }, []);
    return (
        <div>
            Event data:{data}
        </div>
    )
}

export default Sse;
