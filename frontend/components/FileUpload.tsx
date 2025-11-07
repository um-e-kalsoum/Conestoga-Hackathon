'use client';

import { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, FileSpreadsheet, Loader2 } from 'lucide-react';
import { uploadAndAnalyze } from '@/lib/api';
import { AnalysisData } from '@/lib/types';

interface FileUploadProps {
  onAnalysisComplete: (data: AnalysisData) => void;
  loading: boolean;
  setLoading: (loading: boolean) => void;
}

export default function FileUpload({
  onAnalysisComplete,
  loading,
  setLoading,
}: FileUploadProps) {
  const [error, setError] = useState<string | null>(null);

  const onDrop = useCallback(
    async (acceptedFiles: File[]) => {
      const file = acceptedFiles[0];
      if (!file) return;

      setError(null);
      setLoading(true);

      try {
        const formData = new FormData();
        formData.append('file', file);

        const data = await uploadAndAnalyze(formData);
        onAnalysisComplete(data);
      } catch (err: any) {
        // Show the actual error message from backend
        const errorMessage = err.message || 'Failed to process file. Please try again.';
        setError(errorMessage);
        console.error('Upload error:', err);
      } finally {
        setLoading(false);
      }
    },
    [onAnalysisComplete, setLoading]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
      'application/vnd.ms-excel': ['.xls'],
      'text/csv': ['.csv'],
    },
    maxFiles: 1,
    disabled: loading,
  });

  return (
    <div className="max-w-2xl mx-auto">
      <div
        {...getRootProps()}
        className={`
          border-2 border-dashed rounded-lg p-12 text-center cursor-pointer
          transition-all duration-200
          ${
            isDragActive
              ? 'border-primary-500 bg-primary-50'
              : 'border-gray-300 hover:border-primary-400 hover:bg-gray-50'
          }
          ${loading ? 'opacity-50 cursor-not-allowed' : ''}
        `}
      >
        <input {...getInputProps()} />
        {loading ? (
          <div className="flex flex-col items-center">
            <Loader2 className="w-12 h-12 text-primary-500 animate-spin mb-4" />
            <p className="text-lg text-gray-600">Processing your file...</p>
          </div>
        ) : (
          <div className="flex flex-col items-center">
            <FileSpreadsheet className="w-16 h-16 text-primary-500 mb-4" />
            <Upload className="w-8 h-8 text-gray-400 mb-4" />
            <p className="text-lg font-medium text-gray-700 mb-2">
              {isDragActive
                ? 'Drop your file here'
                : 'Drag & drop your Excel/CSV file here'}
            </p>
            <p className="text-sm text-gray-500">
              or click to browse (supports .xlsx, .xls, .csv)
            </p>
          </div>
        )}
      </div>

      {error && (
        <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
          <p className="text-red-800">{error}</p>
        </div>
      )}
    </div>
  );
}

