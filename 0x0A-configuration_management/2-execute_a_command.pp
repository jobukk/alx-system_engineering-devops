exec { 'killmenow':
  command     => 'pkill killmenow',
  refreshonly => true,
}
