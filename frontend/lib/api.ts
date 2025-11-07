import axios from 'axios';
import { AnalysisData } from './types';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function uploadAndAnalyze(file: FormData): Promise<AnalysisData> {
  try {
    const response = await axios.post(`${API_BASE}/api/upload`, file, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error: any) {
    // Extract detailed error message from backend
    if (error.response?.data?.detail) {
      throw new Error(error.response.data.detail);
    } else if (error.message) {
      throw new Error(error.message);
    } else {
      throw new Error('Failed to process file. Please try again.');
    }
  }
}

export async function exportReport(data: AnalysisData): Promise<void> {
  const response = await axios.post(
    `${API_BASE}/api/export`,
    data,
    {
      responseType: 'blob',
    }
  );

  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `zero-waste-report-${Date.now()}.pdf`);
  document.body.appendChild(link);
  link.click();
  link.remove();
}

